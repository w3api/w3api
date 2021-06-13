---
title: BeanContextServiceProvider.getService()
permalink: /Java/BeanContextServiceProvider/getService/
date: 2021-01-11
key: Java.B.BeanContextServiceProvider
category: Java
tags: ['java se', 'java.beans.beancontext', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.B.BeanContextServiceProvider.metodos valor="getService" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
Object getService(BeanContextServices bcs, Object requestor, Class<?> serviceClass, Object serviceSelector)
~~~

## Parámetros
* **Object serviceSelector**,  {% include w3api/param_description.html metodo=_dato parametro="Object serviceSelector" %}
* **Class&lt;?&gt; serviceClass**,  {% include w3api/param_description.html metodo=_dato parametro="Class<?> serviceClass" %}
* **BeanContextServices bcs**,  {% include w3api/param_description.html metodo=_dato parametro="BeanContextServices bcs" %}
* **Object requestor**,  {% include w3api/param_description.html metodo=_dato parametro="Object requestor" %}

## Clase Padre
[BeanContextServiceProvider](/Java/BeanContextServiceProvider/)

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
