---
title: SyncFactory.unregisterProvider()
permalink: Java/SyncFactory/unregisterProvider
date: 2021-01-04
key: JavaJava.S.SyncFactory
category: java
tags: ['java se', 'javax.sql.rowset.spi', 'java.sql.rowset', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SyncFactory.metodos valor="unregisterProvider" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static void unregisterProvider(String providerID) throws SyncFactoryException
~~~

## Parámetros
* **String providerID**,  {% include w3api/param_description.html metodo=_data parametro="String providerID" %}

## Excepciones
[SyncFactoryException](/Java/SyncFactoryException/)

## Clase Padre
[SyncFactory](/Java/SyncFactory/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.SyncFactory.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
