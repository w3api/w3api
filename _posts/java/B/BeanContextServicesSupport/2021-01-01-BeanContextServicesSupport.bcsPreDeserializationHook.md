---
title: BeanContextServicesSupport.bcsPreDeserializationHook()
permalink: /Java/BeanContextServicesSupport/bcsPreDeserializationHook/
date: 2021-01-11
key: Java.B.BeanContextServicesSupport
category: Java
tags: ['java se', 'java.beans.beancontext', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.B.BeanContextServicesSupport.metodos valor="bcsPreDeserializationHook" %}

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
