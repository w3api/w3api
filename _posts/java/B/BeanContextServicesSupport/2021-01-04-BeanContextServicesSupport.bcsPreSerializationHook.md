---
title: BeanContextServicesSupport.bcsPreSerializationHook()
permalink: Java/BeanContextServicesSupport/bcsPreSerializationHook
date: 2021-01-04
key: JavaJava.B.BeanContextServicesSupport
category: java
tags: ['java se', 'java.beans.beancontext', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.B.BeanContextServicesSupport.metodos valor="bcsPreSerializationHook" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected void bcsPreSerializationHook(ObjectOutputStream oos) throws IOException
~~~

## Parámetros
* **ObjectOutputStream oos**,  {% include w3api/param_description.html metodo=_data parametro="ObjectOutputStream oos" %}

## Excepciones
[IOException](/Java/IOException/)

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
