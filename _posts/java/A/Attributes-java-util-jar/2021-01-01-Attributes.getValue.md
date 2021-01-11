---
title: Attributes.getValue()
permalink: Java/Attributes-java-util-jar/getValue
date: 2021-01-11
key: JavaJava.A.Attributes-java-util-jar
category: java
tags: ['java se', 'java.util.jar', 'java.base', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.Attributes-java-util-jar.metodos valor="getValue" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public String getValue(String name)
public String getValue(Attributes.Name name)
~~~

## Parámetros
* **String name**,  {% include w3api/param_description.html metodo=_dato parametro="String name" %}
* **Attributes.Name name**,  {% include w3api/param_description.html metodo=_dato parametro="Attributes.Name name" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[Attributes](/Java/Attributes-java-util-jar/)

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
