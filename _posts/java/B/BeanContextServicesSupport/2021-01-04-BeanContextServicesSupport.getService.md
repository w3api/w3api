---
title: BeanContextServicesSupport.getService()
permalink: Java/BeanContextServicesSupport/getService
date: 2021-01-04
key: JavaJava.B.BeanContextServicesSupport
category: java
tags: ['java se', 'java.beans.beancontext', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.B.BeanContextServicesSupport.metodos valor="getService" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public Object getService(BeanContextChild child, Object requestor, Class<?> serviceClass, Object serviceSelector, BeanContextServiceRevokedListener bcsrl) throws TooManyListenersException
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
