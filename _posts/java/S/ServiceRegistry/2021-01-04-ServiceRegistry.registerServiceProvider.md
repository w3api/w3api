---
title: ServiceRegistry.registerServiceProvider()
permalink: Java/ServiceRegistry/registerServiceProvider
date: 2021-01-04
key: JavaJava.S.ServiceRegistry
category: java
tags: ['java se', 'javax.imageio.spi', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.ServiceRegistry.metodos valor="registerServiceProvider" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void registerServiceProvider(Object provider)
<T> boolean registerServiceProvider(T provider, Class<T> category)
~~~

## Parámetros
* **T provider**,  {% include w3api/param_description.html metodo=_data parametro="T provider" %}
* **Class&lt;T&gt; category**,  {% include w3api/param_description.html metodo=_data parametro="Class<T> category" %}
* **Object provider**,  {% include w3api/param_description.html metodo=_data parametro="Object provider" %}

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
{%- for _ldc in site.data.Java.S.ServiceRegistry.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
