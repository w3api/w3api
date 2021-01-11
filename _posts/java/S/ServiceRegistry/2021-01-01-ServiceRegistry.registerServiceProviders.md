---
title: ServiceRegistry.registerServiceProviders()
permalink: Java/ServiceRegistry/registerServiceProviders
date: 2021-01-11
key: JavaJava.S.ServiceRegistry
category: java
tags: ['java se', 'javax.imageio.spi', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.ServiceRegistry.metodos valor="registerServiceProviders" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void registerServiceProviders(Iterator<?> providers)
~~~

## Parámetros
* **Iterator&lt;?&gt; providers**,  {% include w3api/param_description.html metodo=_dato parametro="Iterator<?> providers" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[ServiceRegistry](/Java/ServiceRegistry/)

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
