---
title: BeanContextSupport.bcsPreSerializationHook()
permalink: /Java/BeanContextSupport/bcsPreSerializationHook/
date: 2021-01-11
key: Java.B.BeanContextSupport
category: Java
tags: ['java se', 'java.beans.beancontext', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.B.BeanContextSupport.metodos valor="bcsPreSerializationHook" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected void bcsPreSerializationHook(ObjectOutputStream oos) throws IOException
~~~

## Parámetros
* **ObjectOutputStream oos**,  {% include w3api/param_description.html metodo=_dato parametro="ObjectOutputStream oos" %}

## Excepciones
[IOException](/Java/IOException/)

## Clase Padre
[BeanContextSupport](/Java/BeanContextSupport/)

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
