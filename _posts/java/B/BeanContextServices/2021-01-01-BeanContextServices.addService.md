---
title: BeanContextServices.addService()
permalink: Java/BeanContextServices/addService
date: 2021-01-11
key: JavaJava.B.BeanContextServices
category: java
tags: ['java se', 'java.beans.beancontext', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.B.BeanContextServices.metodos valor="addService" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
boolean addService(Class<?> serviceClass, BeanContextServiceProvider serviceProvider)
~~~

## Parámetros
* **BeanContextServiceProvider serviceProvider**,  {% include w3api/param_description.html metodo=_dato parametro="BeanContextServiceProvider serviceProvider" %}
* **Class&lt;?&gt; serviceClass**,  {% include w3api/param_description.html metodo=_dato parametro="Class<?> serviceClass" %}

## Clase Padre
[BeanContextServices](/Java/BeanContextServices/)

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
