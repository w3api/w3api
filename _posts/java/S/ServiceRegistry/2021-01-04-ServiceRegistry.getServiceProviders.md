---
title: ServiceRegistry.getServiceProviders()
permalink: Java/ServiceRegistry/getServiceProviders
date: 2021-01-04
key: JavaJava.S.ServiceRegistry
category: java
tags: ['java se', 'javax.imageio.spi', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.ServiceRegistry.metodos valor="getServiceProviders" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
<T> Iterator<T> getServiceProviders(Class<T> category, boolean useOrdering)
<T> Iterator<T> getServiceProviders(Class<T> category, ServiceRegistry.Filter filter, boolean useOrdering)
~~~

## Parámetros
* **ServiceRegistry.Filter filter**,  {% include w3api/param_description.html metodo=_data parametro="ServiceRegistry.Filter filter" %}
* **boolean useOrdering**,  {% include w3api/param_description.html metodo=_data parametro="boolean useOrdering" %}
* **Class&lt;T&gt; category**,  {% include w3api/param_description.html metodo=_data parametro="Class<T> category" %}

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
