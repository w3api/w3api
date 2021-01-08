---
title: SyncFactory
permalink: Java/SyncFactory
date: 2021-01-04
key: JavaJava.S.SyncFactory
category: java
tags: ['java se', 'javax.sql.rowset.spi', 'java.sql.rowset', 'clase java', 'Java 1.5']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.S.SyncFactory.description }}

## Sintaxis
~~~java
public class SyncFactory extends Object
~~~

## Campos
* [ROWSET_SYNC_PROVIDER](/Java/SyncFactory/ROWSET_SYNC_PROVIDER)
* [ROWSET_SYNC_PROVIDER_VERSION](/Java/SyncFactory/ROWSET_SYNC_PROVIDER_VERSION)
* [ROWSET_SYNC_VENDOR](/Java/SyncFactory/ROWSET_SYNC_VENDOR)

## Métodos
* [getInstance()](/Java/SyncFactory/getInstance)
* [getLogger()](/Java/SyncFactory/getLogger)
* [getRegisteredProviders()](/Java/SyncFactory/getRegisteredProviders)
* [getSyncFactory()](/Java/SyncFactory/getSyncFactory)
* [registerProvider()](/Java/SyncFactory/registerProvider)
* [setJNDIContext()](/Java/SyncFactory/setJNDIContext)
* [setLogger()](/Java/SyncFactory/setLogger)
* [unregisterProvider()](/Java/SyncFactory/unregisterProvider)

## Ejemplo
~~~java
{{ site.data.Java.S.SyncFactory.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.SyncFactory.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
