---
title: RowIdLifetime
permalink: Java/RowIdLifetime
date: 2021-01-11
key: Java.R.RowIdLifetime
category: java
tags: ['java se', 'java.sql', 'java.sql', 'enumerado java', 'Java 1.6']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.R.RowIdLifetime.description }}

## Sintaxis
~~~java
public enum RowIdLifetime extends Enum<RowIdLifetime>
~~~

## Enumerados
* [ROWID_UNSUPPORTED](/Java/RowIdLifetime/ROWID_UNSUPPORTED)
* [ROWID_VALID_FOREVER](/Java/RowIdLifetime/ROWID_VALID_FOREVER)
* [ROWID_VALID_OTHER](/Java/RowIdLifetime/ROWID_VALID_OTHER)
* [ROWID_VALID_SESSION](/Java/RowIdLifetime/ROWID_VALID_SESSION)
* [ROWID_VALID_TRANSACTION](/Java/RowIdLifetime/ROWID_VALID_TRANSACTION)

## Métodos
* [valueOf()](/Java/RowIdLifetime/valueOf)
* [values()](/Java/RowIdLifetime/values)

## Ejemplo
~~~java
{{ site.data.Java.R.RowIdLifetime.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.R.RowIdLifetime.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
