---
title: BeanContext.getResource()
permalink: /Java/BeanContext/getResource/
date: 2021-01-11
key: Java.B.BeanContext
category: java
tags: ['java se', 'java.beans.beancontext', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.B.BeanContext.metodos valor="getResource" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
URL getResource(String name, BeanContextChild bcc) throws IllegalArgumentException
~~~

## Parámetros
* **String name**,  {% include w3api/param_description.html metodo=_dato parametro="String name" %}
* **BeanContextChild bcc**,  {% include w3api/param_description.html metodo=_dato parametro="BeanContextChild bcc" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[BeanContext](/Java/BeanContext/)

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
