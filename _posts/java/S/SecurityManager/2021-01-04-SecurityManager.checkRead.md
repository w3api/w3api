---
title: SecurityManager.checkRead()
permalink: Java/SecurityManager/checkRead
date: 2021-01-04
key: JavaJava.S.SecurityManager
category: java
tags: ['java se', 'java.lang', 'java.base', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SecurityManager.metodos valor="checkRead" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void checkRead(FileDescriptor fd)
public void checkRead(String file)
public void checkRead(String file, Object context)
~~~

## Parámetros
* **String file**,  {% include w3api/param_description.html metodo=_data parametro="String file" %}
* **Object context**,  {% include w3api/param_description.html metodo=_data parametro="Object context" %}
* **FileDescriptor fd**,  {% include w3api/param_description.html metodo=_data parametro="FileDescriptor fd" %}

## Excepciones
[SecurityException](/Java/SecurityException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[SecurityManager](/Java/SecurityManager/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.SecurityManager.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
