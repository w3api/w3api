---
title: BeanContextServicesSupport.fireServiceRevoked()
permalink: Java/BeanContextServicesSupport/fireServiceRevoked
date: 2021-01-04
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
* **Class&lt;?&gt; serviceClass**,  {% include w3api/param_description.html metodo=_data parametro="Class<?> serviceClass" %}
* **BeanContextServiceRevokedEvent bcsre**,  {% include w3api/param_description.html metodo=_data parametro="BeanContextServiceRevokedEvent bcsre" %}
* **boolean revokeNow**,  {% include w3api/param_description.html metodo=_data parametro="boolean revokeNow" %}

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
