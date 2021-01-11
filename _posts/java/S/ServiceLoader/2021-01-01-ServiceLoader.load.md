---
title: ServiceLoader.load()
permalink: Java/ServiceLoader/load
date: 2021-01-11
key: JavaJava.S.ServiceLoader
category: java
tags: ['java se', 'java.util', 'java.base', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.ServiceLoader.metodos valor="load" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
static <S> ServiceLoader<S> load(Class<S> service)
static <S> ServiceLoader<S> load(Class<S> service, ClassLoader loader)
static <S> ServiceLoader<S> load(ModuleLayer layer, Class<S> service)
~~~

## Parámetros
* **Class&lt;S&gt; service**,  {% include w3api/param_description.html metodo=_dato parametro="Class<S> service" %}
* **ModuleLayer layer**,  {% include w3api/param_description.html metodo=_dato parametro="ModuleLayer layer" %}
* **ClassLoader loader**,  {% include w3api/param_description.html metodo=_dato parametro="ClassLoader loader" %}

## Clase Padre
[ServiceLoader](/Java/ServiceLoader/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
