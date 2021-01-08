---
title: BeanContextServiceProvider.getService()
permalink: Java/BeanContextServiceProvider/getService
date: 2021-01-04
key: JavaJava.B.BeanContextServiceProvider
category: java
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
* **BeanContextServices bcs**,  {% include w3api/param_description.html metodo=_data parametro="BeanContextServices bcs" %}
* **Class&lt;?&gt; serviceClass**,  {% include w3api/param_description.html metodo=_data parametro="Class<?> serviceClass" %}
* **Object requestor**,  {% include w3api/param_description.html metodo=_data parametro="Object requestor" %}
* **Object serviceSelector**,  {% include w3api/param_description.html metodo=_data parametro="Object serviceSelector" %}

## Clase Padre
[BeanContextServiceProvider](/Java/BeanContextServiceProvider/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.B.BeanContextServiceProvider.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
