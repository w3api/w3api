---
title: BeanContextServicesSupport.addService()
permalink: /Java/BeanContextServicesSupport/addService/
date: 2021-01-11
key: Java.B.BeanContextServicesSupport
category: Java
tags: ['java se', 'java.beans.beancontext', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.B.BeanContextServicesSupport.metodos valor="addService" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public boolean addService(Class<?> serviceClass, BeanContextServiceProvider bcsp)
protected boolean addService(Class<?> serviceClass, BeanContextServiceProvider bcsp, boolean fireEvent)
~~~

## Parámetros
* **BeanContextServiceProvider bcsp**,  {% include w3api/param_description.html metodo=_dato parametro="BeanContextServiceProvider bcsp" %}
* **boolean fireEvent**,  {% include w3api/param_description.html metodo=_dato parametro="boolean fireEvent" %}
* **Class&lt;?&gt; serviceClass**,  {% include w3api/param_description.html metodo=_dato parametro="Class<?> serviceClass" %}

## Clase Padre
[BeanContextServicesSupport](/Java/BeanContextServicesSupport/)

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
