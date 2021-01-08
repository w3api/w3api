---
title: ServiceRegistry.lookupProviders()
permalink: Java/ServiceRegistry/lookupProviders
date: 2021-01-04
key: JavaJava.S.ServiceRegistry
category: java
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
* **Class&lt;T&gt; providerClass**,  {% include w3api/param_description.html metodo=_data parametro="Class<T> providerClass" %}
* **ClassLoader loader**,  {% include w3api/param_description.html metodo=_data parametro="ClassLoader loader" %}

## Clase Padre
[ServiceRegistry](/Java/ServiceRegistry/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.ServiceRegistry.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
