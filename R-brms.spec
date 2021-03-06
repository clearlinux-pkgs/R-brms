#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-brms
Version  : 2.15.0
Release  : 60
URL      : https://cran.r-project.org/src/contrib/brms_2.15.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/brms_2.15.0.tar.gz
Summary  : Bayesian Regression Models using 'Stan'
Group    : Development/Tools
License  : GPL-2.0
Requires: R-Rcpp
Requires: R-abind
Requires: R-backports
Requires: R-bayesplot
Requires: R-bridgesampling
Requires: R-coda
Requires: R-future
Requires: R-ggplot2
Requires: R-glue
Requires: R-loo
Requires: R-matrixStats
Requires: R-nleqslv
Requires: R-projpred
Requires: R-rstan
Requires: R-rstantools
Requires: R-shinystan
BuildRequires : R-Rcpp
BuildRequires : R-abind
BuildRequires : R-backports
BuildRequires : R-bayesplot
BuildRequires : R-bridgesampling
BuildRequires : R-coda
BuildRequires : R-future
BuildRequires : R-ggplot2
BuildRequires : R-glue
BuildRequires : R-loo
BuildRequires : R-matrixStats
BuildRequires : R-nleqslv
BuildRequires : R-projpred
BuildRequires : R-rstan
BuildRequires : R-rstantools
BuildRequires : R-shinystan
BuildRequires : buildreq-R

%description
Fit Bayesian generalized (non-)linear multivariate multilevel models using
'Stan' for full Bayesian inference. A wide range of distributions and link
functions are supported, allowing users to fit – among others – linear, robust
linear, count data, survival, response times, ordinal, zero-inflated, hurdle,
and even self-defined mixture models all in a multilevel context. Further
modeling options include non-linear and smooth terms, auto-correlation
structures, censored data, meta-analytic standard errors, and quite a few more.
In addition, all parameters of the response distribution can be predicted in
order to perform distributional regression. Prior specifications are flexible
and explicitly encourage users to apply prior distributions that actually
reflect their beliefs. Model fit can easily be assessed and compared with
posterior predictive checks and leave-one-out cross-validation.

%prep
%setup -q -c -n brms
cd %{_builddir}/brms

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1615821170

%install
export SOURCE_DATE_EPOCH=1615821170
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library brms
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library brms
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library brms
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc brms || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/brms/CITATION
/usr/lib64/R/library/brms/DESCRIPTION
/usr/lib64/R/library/brms/INDEX
/usr/lib64/R/library/brms/Meta/Rd.rds
/usr/lib64/R/library/brms/Meta/data.rds
/usr/lib64/R/library/brms/Meta/features.rds
/usr/lib64/R/library/brms/Meta/hsearch.rds
/usr/lib64/R/library/brms/Meta/links.rds
/usr/lib64/R/library/brms/Meta/nsInfo.rds
/usr/lib64/R/library/brms/Meta/package.rds
/usr/lib64/R/library/brms/Meta/vignette.rds
/usr/lib64/R/library/brms/NAMESPACE
/usr/lib64/R/library/brms/NEWS.md
/usr/lib64/R/library/brms/R/brms
/usr/lib64/R/library/brms/R/brms.rdb
/usr/lib64/R/library/brms/R/brms.rdx
/usr/lib64/R/library/brms/R/sysdata.rdb
/usr/lib64/R/library/brms/R/sysdata.rdx
/usr/lib64/R/library/brms/chunks/fun_asym_laplace.stan
/usr/lib64/R/library/brms/chunks/fun_cauchit.stan
/usr/lib64/R/library/brms/chunks/fun_cholesky_cor_ar1.stan
/usr/lib64/R/library/brms/chunks/fun_cholesky_cor_arma1.stan
/usr/lib64/R/library/brms/chunks/fun_cholesky_cor_cosy.stan
/usr/lib64/R/library/brms/chunks/fun_cholesky_cor_ma1.stan
/usr/lib64/R/library/brms/chunks/fun_cloglog.stan
/usr/lib64/R/library/brms/chunks/fun_com_poisson.stan
/usr/lib64/R/library/brms/chunks/fun_cox.stan
/usr/lib64/R/library/brms/chunks/fun_dirichlet_logit.stan
/usr/lib64/R/library/brms/chunks/fun_discrete_weibull.stan
/usr/lib64/R/library/brms/chunks/fun_gaussian_process.stan
/usr/lib64/R/library/brms/chunks/fun_gaussian_process_approx.stan
/usr/lib64/R/library/brms/chunks/fun_gen_extreme_value.stan
/usr/lib64/R/library/brms/chunks/fun_horseshoe.stan
/usr/lib64/R/library/brms/chunks/fun_hurdle_gamma.stan
/usr/lib64/R/library/brms/chunks/fun_hurdle_lognormal.stan
/usr/lib64/R/library/brms/chunks/fun_hurdle_negbinomial.stan
/usr/lib64/R/library/brms/chunks/fun_hurdle_poisson.stan
/usr/lib64/R/library/brms/chunks/fun_inv_gaussian.stan
/usr/lib64/R/library/brms/chunks/fun_logm1.stan
/usr/lib64/R/library/brms/chunks/fun_monotonic.stan
/usr/lib64/R/library/brms/chunks/fun_multinomial_logit.stan
/usr/lib64/R/library/brms/chunks/fun_normal_errorsar.stan
/usr/lib64/R/library/brms/chunks/fun_normal_fcor.stan
/usr/lib64/R/library/brms/chunks/fun_normal_lagsar.stan
/usr/lib64/R/library/brms/chunks/fun_normal_time.stan
/usr/lib64/R/library/brms/chunks/fun_r2d2.stan
/usr/lib64/R/library/brms/chunks/fun_scale_r_cor.stan
/usr/lib64/R/library/brms/chunks/fun_scale_r_cor_by.stan
/usr/lib64/R/library/brms/chunks/fun_scale_r_cor_by_cov.stan
/usr/lib64/R/library/brms/chunks/fun_scale_r_cor_cov.stan
/usr/lib64/R/library/brms/chunks/fun_scale_time_err.stan
/usr/lib64/R/library/brms/chunks/fun_scale_xi.stan
/usr/lib64/R/library/brms/chunks/fun_sequence.stan
/usr/lib64/R/library/brms/chunks/fun_softplus.stan
/usr/lib64/R/library/brms/chunks/fun_sparse_car_lpdf.stan
/usr/lib64/R/library/brms/chunks/fun_sparse_icar_lpdf.stan
/usr/lib64/R/library/brms/chunks/fun_student_t_errorsar.stan
/usr/lib64/R/library/brms/chunks/fun_student_t_fcor.stan
/usr/lib64/R/library/brms/chunks/fun_student_t_lagsar.stan
/usr/lib64/R/library/brms/chunks/fun_student_t_time.stan
/usr/lib64/R/library/brms/chunks/fun_tan_half.stan
/usr/lib64/R/library/brms/chunks/fun_von_mises.stan
/usr/lib64/R/library/brms/chunks/fun_which_range.stan
/usr/lib64/R/library/brms/chunks/fun_wiener_diffusion.stan
/usr/lib64/R/library/brms/chunks/fun_zero_inflated_asym_laplace.stan
/usr/lib64/R/library/brms/chunks/fun_zero_inflated_beta.stan
/usr/lib64/R/library/brms/chunks/fun_zero_inflated_binomial.stan
/usr/lib64/R/library/brms/chunks/fun_zero_inflated_negbinomial.stan
/usr/lib64/R/library/brms/chunks/fun_zero_inflated_poisson.stan
/usr/lib64/R/library/brms/chunks/fun_zero_one_inflated_beta.stan
/usr/lib64/R/library/brms/data/Rdata.rdb
/usr/lib64/R/library/brms/data/Rdata.rds
/usr/lib64/R/library/brms/data/Rdata.rdx
/usr/lib64/R/library/brms/doc/brms_customfamilies.R
/usr/lib64/R/library/brms/doc/brms_customfamilies.Rmd
/usr/lib64/R/library/brms/doc/brms_customfamilies.html
/usr/lib64/R/library/brms/doc/brms_distreg.R
/usr/lib64/R/library/brms/doc/brms_distreg.Rmd
/usr/lib64/R/library/brms/doc/brms_distreg.html
/usr/lib64/R/library/brms/doc/brms_families.Rmd
/usr/lib64/R/library/brms/doc/brms_families.html
/usr/lib64/R/library/brms/doc/brms_missings.R
/usr/lib64/R/library/brms/doc/brms_missings.Rmd
/usr/lib64/R/library/brms/doc/brms_missings.html
/usr/lib64/R/library/brms/doc/brms_monotonic.R
/usr/lib64/R/library/brms/doc/brms_monotonic.Rmd
/usr/lib64/R/library/brms/doc/brms_monotonic.html
/usr/lib64/R/library/brms/doc/brms_multilevel.ltx
/usr/lib64/R/library/brms/doc/brms_multilevel.pdf
/usr/lib64/R/library/brms/doc/brms_multivariate.R
/usr/lib64/R/library/brms/doc/brms_multivariate.Rmd
/usr/lib64/R/library/brms/doc/brms_multivariate.html
/usr/lib64/R/library/brms/doc/brms_nonlinear.R
/usr/lib64/R/library/brms/doc/brms_nonlinear.Rmd
/usr/lib64/R/library/brms/doc/brms_nonlinear.html
/usr/lib64/R/library/brms/doc/brms_overview.ltx
/usr/lib64/R/library/brms/doc/brms_overview.pdf
/usr/lib64/R/library/brms/doc/brms_phylogenetics.R
/usr/lib64/R/library/brms/doc/brms_phylogenetics.Rmd
/usr/lib64/R/library/brms/doc/brms_phylogenetics.html
/usr/lib64/R/library/brms/doc/brms_threading.R
/usr/lib64/R/library/brms/doc/brms_threading.Rmd
/usr/lib64/R/library/brms/doc/brms_threading.html
/usr/lib64/R/library/brms/doc/index.html
/usr/lib64/R/library/brms/help/AnIndex
/usr/lib64/R/library/brms/help/aliases.rds
/usr/lib64/R/library/brms/help/brms.rdb
/usr/lib64/R/library/brms/help/brms.rdx
/usr/lib64/R/library/brms/help/figures/README-conditional_effects-1.png
/usr/lib64/R/library/brms/help/figures/README-plot-1.png
/usr/lib64/R/library/brms/help/figures/brms.png
/usr/lib64/R/library/brms/help/figures/stanlogo.png
/usr/lib64/R/library/brms/help/paths.rds
/usr/lib64/R/library/brms/html/00Index.html
/usr/lib64/R/library/brms/html/R.css
/usr/lib64/R/library/brms/tests/testthat.R
/usr/lib64/R/library/brms/tests/testthat/tests.brm.R
/usr/lib64/R/library/brms/tests/testthat/tests.brmsfit-helpers.R
/usr/lib64/R/library/brms/tests/testthat/tests.brmsfit-methods.R
/usr/lib64/R/library/brms/tests/testthat/tests.brmsformula.R
/usr/lib64/R/library/brms/tests/testthat/tests.brmsterms.R
/usr/lib64/R/library/brms/tests/testthat/tests.data-helpers.R
/usr/lib64/R/library/brms/tests/testthat/tests.distributions.R
/usr/lib64/R/library/brms/tests/testthat/tests.emmeans.R
/usr/lib64/R/library/brms/tests/testthat/tests.exclude_pars.R
/usr/lib64/R/library/brms/tests/testthat/tests.families.R
/usr/lib64/R/library/brms/tests/testthat/tests.log_lik.R
/usr/lib64/R/library/brms/tests/testthat/tests.make_stancode.R
/usr/lib64/R/library/brms/tests/testthat/tests.make_standata.R
/usr/lib64/R/library/brms/tests/testthat/tests.misc.R
/usr/lib64/R/library/brms/tests/testthat/tests.posterior_epred.R
/usr/lib64/R/library/brms/tests/testthat/tests.posterior_predict.R
/usr/lib64/R/library/brms/tests/testthat/tests.priors.R
/usr/lib64/R/library/brms/tests/testthat/tests.rename_pars.R
/usr/lib64/R/library/brms/tests/testthat/tests.restructure.R
/usr/lib64/R/library/brms/tests/testthat/tests.stan_functions.R
