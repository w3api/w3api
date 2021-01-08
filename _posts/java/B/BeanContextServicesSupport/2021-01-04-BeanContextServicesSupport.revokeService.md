---
title: BeanContextServicesSupport.revokeService()
permalink: Java/BeanContextServicesSupport/revokeService
date: 2021-01-04
key: JavaJava.B.BeanContextServicesSupport
category: java
tags: ['java se', 'java.beans.beancontext', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.B.BeanContextServicesSupport.metodos valor="revokeService" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void revokeService(Class<?> serviceClass, BeanContextServiceProvider bcsp, boolean revokeCurrentServicesNow)
~~~

## Parámetros
* **BeanContextServiceProvider bcsp**,  {% include w3api/param_description.html metodo=_data parametro="BeanContextServiceProvider bcsp" %}
* **Class&lt;?&gt; serviceClass**,  {% include w3api/param_description.html metodo=_data parametro="Class<?> serviceClass" %}
* **boolean revokeCurrentServicesNow**,  {% include w3api/param_description.html metodo=_data parametro="boolean revokeCurrentServicesNow" %}

## Clase Padre
[BeanContextServicesSupport](/Java/BeanContextServicesSupport/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.B.BeanContextServicesSupport.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
