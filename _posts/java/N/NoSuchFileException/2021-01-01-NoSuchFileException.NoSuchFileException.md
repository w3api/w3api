---
title: NoSuchFileException.NoSuchFileException()
permalink: Java/NoSuchFileException/NoSuchFileException
date: 2021-01-11
key: JavaJava.N.NoSuchFileException
category: Java
tags: ['java se', 'java.nio.file', 'java.base', 'metodo java', 'Java 1.7']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.N.NoSuchFileException.constructores valor="NoSuchFileException" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public NoSuchFileException(String file)
public NoSuchFileException(String file, String other, String reason)
~~~

## Parámetros
* **String reason**,  {% include w3api/param_description.html metodo=_dato parametro="String reason" %}
* **String file**,  {% include w3api/param_description.html metodo=_dato parametro="String file" %}
* **String other**,  {% include w3api/param_description.html metodo=_dato parametro="String other" %}

## Clase Padre
[NoSuchFileException](/Java/NoSuchFileException/)

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
