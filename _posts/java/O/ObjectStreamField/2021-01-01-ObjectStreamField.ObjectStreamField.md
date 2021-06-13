---
title: ObjectStreamField.ObjectStreamField()
permalink: /Java/ObjectStreamField/ObjectStreamField/
date: 2021-01-11
key: JavaJava.O.ObjectStreamField
category: java
tags: ['java se', 'java.io', 'java.base', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.O.ObjectStreamField.constructores valor="ObjectStreamField" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public ObjectStreamField(String name, Class<?> type)
public ObjectStreamField(String name, Class<?> type, boolean unshared)
~~~

## Parámetros
* **String name**,  {% include w3api/param_description.html metodo=_dato parametro="String name" %}
* **Class&lt;?&gt; type**,  {% include w3api/param_description.html metodo=_dato parametro="Class<?> type" %}
* **boolean unshared**,  {% include w3api/param_description.html metodo=_dato parametro="boolean unshared" %}

## Clase Padre
[ObjectStreamField](/Java/ObjectStreamField/)

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
