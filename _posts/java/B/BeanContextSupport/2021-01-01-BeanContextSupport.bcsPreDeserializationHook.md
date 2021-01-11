---
title: BeanContextSupport.bcsPreDeserializationHook()
permalink: Java/BeanContextSupport/bcsPreDeserializationHook
date: 2021-01-11
key: JavaJava.B.BeanContextSupport
category: java
tags: ['java se', 'java.beans.beancontext', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.B.BeanContextSupport.metodos valor="bcsPreDeserializationHook" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected void bcsPreDeserializationHook(ObjectInputStream ois) throws IOException, ClassNotFoundException
~~~

## Parámetros
* **ObjectInputStream ois**,  {% include w3api/param_description.html metodo=_dato parametro="ObjectInputStream ois" %}

## Excepciones
[ClassNotFoundException](/Java/ClassNotFoundException/), [IOException](/Java/IOException/)

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
