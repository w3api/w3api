---
title: ServiceRegistry.setOrdering()
permalink: Java/ServiceRegistry/setOrdering
date: 2021-01-11
key: JavaJava.S.ServiceRegistry
category: java
tags: ['java se', 'javax.imageio.spi', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.ServiceRegistry.metodos valor="setOrdering" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
<T> boolean setOrdering(Class<T> category, T firstProvider, T secondProvider)
~~~

## Parámetros
* **T firstProvider**,  {% include w3api/param_description.html metodo=_dato parametro="T firstProvider" %}
* **Class&lt;T&gt; category**,  {% include w3api/param_description.html metodo=_dato parametro="Class<T> category" %}
* **T secondProvider**,  {% include w3api/param_description.html metodo=_dato parametro="T secondProvider" %}

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
