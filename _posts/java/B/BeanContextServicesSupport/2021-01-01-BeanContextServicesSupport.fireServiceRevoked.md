---
title: BeanContextServicesSupport.fireServiceRevoked()
permalink: /Java/BeanContextServicesSupport/fireServiceRevoked/
date: 2021-01-11
key: JavaJava.B.BeanContextServicesSupport
category: java
tags: ['java se', 'java.beans.beancontext', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.B.BeanContextServicesSupport.metodos valor="fireServiceRevoked" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected void fireServiceRevoked(BeanContextServiceRevokedEvent bcsre)
protected void fireServiceRevoked(Class<?> serviceClass, boolean revokeNow)
~~~

## Parámetros
* **BeanContextServiceRevokedEvent bcsre**,  {% include w3api/param_description.html metodo=_dato parametro="BeanContextServiceRevokedEvent bcsre" %}
* **boolean revokeNow**,  {% include w3api/param_description.html metodo=_dato parametro="boolean revokeNow" %}
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
