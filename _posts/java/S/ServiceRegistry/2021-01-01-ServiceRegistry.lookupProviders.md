---
title: ServiceRegistry.lookupProviders()
permalink: /Java/ServiceRegistry/lookupProviders/
date: 2021-01-11
key: Java.S.ServiceRegistry
category: Java
tags: ['java se', 'javax.imageio.spi', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.ServiceRegistry.metodos valor="lookupProviders" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
static <T> Iterator<T> lookupProviders(Class<T> providerClass)
static <T> Iterator<T> lookupProviders(Class<T> providerClass, ClassLoader loader)
~~~

## Parámetros
* **ClassLoader loader**,  {% include w3api/param_description.html metodo=_dato parametro="ClassLoader loader" %}
* **Class&lt;T&gt; providerClass**,  {% include w3api/param_description.html metodo=_dato parametro="Class<T> providerClass" %}

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
