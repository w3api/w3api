---
title: BeanContextServices.getService()
permalink: /Java/BeanContextServices/getService/
date: 2021-01-11
key: Java.B.BeanContextServices
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
* **Object serviceSelector**,  {% include w3api/param_description.html metodo=_dato parametro="Object serviceSelector" %}
* **Object requestor**,  {% include w3api/param_description.html metodo=_dato parametro="Object requestor" %}
* **BeanContextServiceRevokedListener bcsrl**,  {% include w3api/param_description.html metodo=_dato parametro="BeanContextServiceRevokedListener bcsrl" %}
* **BeanContextChild child**,  {% include w3api/param_description.html metodo=_dato parametro="BeanContextChild child" %}
* **Class&lt;?&gt; serviceClass**,  {% include w3api/param_description.html metodo=_dato parametro="Class<?> serviceClass" %}

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
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
