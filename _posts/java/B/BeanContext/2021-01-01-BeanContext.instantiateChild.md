---
title: BeanContext.instantiateChild()
permalink: /Java/BeanContext/instantiateChild/
date: 2021-01-11
key: Java.B.BeanContext
category: Java
tags: ['java se', 'java.beans.beancontext', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.B.BeanContext.metodos valor="instantiateChild" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
Object instantiateChild(String beanName) throws IOException, ClassNotFoundException
~~~

## Parámetros
* **String beanName**,  {% include w3api/param_description.html metodo=_dato parametro="String beanName" %}

## Excepciones
[ClassNotFoundException](/Java/ClassNotFoundException/), [IOException](/Java/IOException/)

## Clase Padre
[BeanContext](/Java/BeanContext/)

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
