---
title: ServiceRegistry.deregisterServiceProvider()
permalink: /Java/ServiceRegistry/deregisterServiceProvider/
date: 2021-01-11
key: Java.S.ServiceRegistry
category: Java
tags: ['java se', 'javax.imageio.spi', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.ServiceRegistry.metodos valor="deregisterServiceProvider" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void deregisterServiceProvider(Object provider)
<T> boolean deregisterServiceProvider(T provider, Class<T> category)
~~~

## Parámetros
* **Class&lt;T&gt; category**,  {% include w3api/param_description.html metodo=_dato parametro="Class<T> category" %}
* **Object provider**,  {% include w3api/param_description.html metodo=_dato parametro="Object provider" %}
* **T provider**,  {% include w3api/param_description.html metodo=_dato parametro="T provider" %}

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
