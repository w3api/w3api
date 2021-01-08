---
title: ScheduledService
permalink: Java/ScheduledService
date: 2021-01-04
key: JavaJava.S.ScheduledService
category: java
tags: ['java se', 'javafx.concurrent', 'javafx.graphics', 'clase java', 'JavaFX 8.0']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.S.ScheduledService.description }}

## Sintaxis
~~~java
public abstract class ScheduledService<V> extends Service<V>
~~~

## Constructores
* [ScheduledService()](/Java/ScheduledService/ScheduledService/)

## Campos
* [EXPONENTIAL_BACKOFF_STRATEGY](/Java/ScheduledService/EXPONENTIAL_BACKOFF_STRATEGY)
* [LINEAR_BACKOFF_STRATEGY](/Java/ScheduledService/LINEAR_BACKOFF_STRATEGY)
* [LOGARITHMIC_BACKOFF_STRATEGY](/Java/ScheduledService/LOGARITHMIC_BACKOFF_STRATEGY)

## Métodos
* [backoffStrategyProperty()](/Java/ScheduledService/backoffStrategyProperty)
* [cancel()](/Java/ScheduledService/cancel)
* [cumulativePeriodProperty()](/Java/ScheduledService/cumulativePeriodProperty)
* [currentFailureCountProperty()](/Java/ScheduledService/currentFailureCountProperty)
* [delayProperty()](/Java/ScheduledService/delayProperty)
* [failed()](/Java/ScheduledService/failed)
* [getBackoffStrategy()](/Java/ScheduledService/getBackoffStrategy)
* [getCumulativePeriod()](/Java/ScheduledService/getCumulativePeriod)
* [getCurrentFailureCount()](/Java/ScheduledService/getCurrentFailureCount)
* [getDelay()](/Java/ScheduledService/getDelay)
* [getLastValue()](/Java/ScheduledService/getLastValue)
* [getMaximumCumulativePeriod()](/Java/ScheduledService/getMaximumCumulativePeriod)
* [getMaximumFailureCount()](/Java/ScheduledService/getMaximumFailureCount)
* [getPeriod()](/Java/ScheduledService/getPeriod)
* [getRestartOnFailure()](/Java/ScheduledService/getRestartOnFailure)
* [lastValueProperty()](/Java/ScheduledService/lastValueProperty)
* [maximumCumulativePeriodProperty()](/Java/ScheduledService/maximumCumulativePeriodProperty)
* [maximumFailureCountProperty()](/Java/ScheduledService/maximumFailureCountProperty)
* [periodProperty()](/Java/ScheduledService/periodProperty)
* [reset()](/Java/ScheduledService/reset)
* [restartOnFailureProperty()](/Java/ScheduledService/restartOnFailureProperty)
* [setBackoffStrategy()](/Java/ScheduledService/setBackoffStrategy)
* [setDelay()](/Java/ScheduledService/setDelay)
* [setMaximumCumulativePeriod()](/Java/ScheduledService/setMaximumCumulativePeriod)
* [setMaximumFailureCount()](/Java/ScheduledService/setMaximumFailureCount)
* [setPeriod()](/Java/ScheduledService/setPeriod)
* [setRestartOnFailure()](/Java/ScheduledService/setRestartOnFailure)
* [succeeded()](/Java/ScheduledService/succeeded)

## Ejemplo
~~~java
{{ site.data.Java.S.ScheduledService.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.ScheduledService.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
