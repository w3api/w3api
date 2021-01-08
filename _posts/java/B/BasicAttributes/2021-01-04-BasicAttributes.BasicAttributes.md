---
title: BasicAttributes.BasicAttributes()
permalink: Java/BasicAttributes/BasicAttributes
date: 2021-01-04
key: JavaJava.B.BasicAttributes
category: java
tags: ['java se', 'javax.naming.directory', 'java.naming', 'metodo java', 'Java 1.3']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.B.BasicAttributes.constructores valor="BasicAttributes" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public BasicAttributes()
public BasicAttributes(boolean ignoreCase)
public BasicAttributes(String attrID, Object val)
public BasicAttributes(String attrID, Object val, boolean ignoreCase)
~~~

## Parámetros
* **String attrID**,  {% include w3api/param_description.html metodo=_data parametro="String attrID" %}
* **Object val**,  {% include w3api/param_description.html metodo=_data parametro="Object val" %}
* **boolean ignoreCase**,  {% include w3api/param_description.html metodo=_data parametro="boolean ignoreCase" %}

## Clase Padre
[BasicAttributes](/Java/BasicAttributes/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.B.BasicAttributes.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
