---
title: ServiceRegistry.unsetOrdering()
permalink: Java/ServiceRegistry/unsetOrdering
date: 2021-01-04
key: JavaJava.S.ServiceRegistry
category: java
tags: ['java se', 'javax.imageio.spi', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.ServiceRegistry.metodos valor="unsetOrdering" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
<T> boolean unsetOrdering(Class<T> category, T firstProvider, T secondProvider)
~~~

## Parámetros
* **T secondProvider**,  {% include w3api/param_description.html metodo=_data parametro="T secondProvider" %}
* **Class&lt;T&gt; category**,  {% include w3api/param_description.html metodo=_data parametro="Class<T> category" %}
* **T firstProvider**,  {% include w3api/param_description.html metodo=_data parametro="T firstProvider" %}

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
