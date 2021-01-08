---
title: SyncProviderException.SyncProviderException()
permalink: Java/SyncProviderException/SyncProviderException
date: 2021-01-04
key: JavaJava.S.SyncProviderException
category: java
tags: ['java se', 'javax.sql.rowset.spi', 'java.sql.rowset', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SyncProviderException.constructores valor="SyncProviderException" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public SyncProviderException()
public SyncProviderException(String msg)
public SyncProviderException(SyncResolver syncResolver)
~~~

## Parámetros
* **String msg**,  {% include w3api/param_description.html metodo=_data parametro="String msg" %}
* **SyncResolver syncResolver**,  {% include w3api/param_description.html metodo=_data parametro="SyncResolver syncResolver" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[SyncProviderException](/Java/SyncProviderException/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.SyncProviderException.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
