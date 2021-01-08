---
title: BeanContextServices.getService()
permalink: Java/BeanContextServices/getService
date: 2021-01-04
key: JavaJava.B.BeanContextServices
category: java
tags: ['java se', 'java.beans.beancontext', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.B.BeanContextServices.metodos valor="getService" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
Object getService(BeanContextChild child, Object requestor, Class<?> serviceClass, Object serviceSelector, BeanContextServiceRevokedListener bcsrl) throws TooManyListenersException
~~~

## Parámetros
* **Object requestor**,  {% include w3api/param_description.html metodo=_data parametro="Object requestor" %}
* **Class&lt;?&gt; serviceClass**,  {% include w3api/param_description.html metodo=_data parametro="Class<?> serviceClass" %}
* **Object serviceSelector**,  {% include w3api/param_description.html metodo=_data parametro="Object serviceSelector" %}
* **BeanContextServiceRevokedListener bcsrl**,  {% include w3api/param_description.html metodo=_data parametro="BeanContextServiceRevokedListener bcsrl" %}
* **BeanContextChild child**,  {% include w3api/param_description.html metodo=_data parametro="BeanContextChild child" %}

## Excepciones
[TooManyListenersException](/Java/TooManyListenersException/)

## Clase Padre
[BeanContextServices](/Java/BeanContextServices/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.B.BeanContextServices.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
