---
title: ServiceLoader.loadInstalled()
permalink: Java/ServiceLoader/loadInstalled
date: 2021-01-04
key: JavaJava.S.ServiceLoader
category: java
tags: ['java se', 'java.util', 'java.base', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.ServiceLoader.metodos valor="loadInstalled" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
static <S> ServiceLoader<S> loadInstalled(Class<S> service)
~~~

## Parámetros
* **Class&lt;S&gt; service**,  {% include w3api/param_description.html metodo=_data parametro="Class<S> service" %}

## Clase Padre
[ServiceLoader](/Java/ServiceLoader/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.ServiceLoader.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
