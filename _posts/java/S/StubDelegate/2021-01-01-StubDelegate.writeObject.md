---
title: StubDelegate.writeObject()
permalink: Java/StubDelegate/writeObject
date: 2021-01-11
key: JavaJava.S.StubDelegate
category: java
tags: ['java se', 'javax.rmi.CORBA', 'java.corba', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.StubDelegate.metodos valor="writeObject" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void writeObject(Stub self, ObjectOutputStream s) throws IOException
~~~

## Parámetros
* **Stub self**,  {% include w3api/param_description.html metodo=_dato parametro="Stub self" %}
* **ObjectOutputStream s**,  {% include w3api/param_description.html metodo=_dato parametro="ObjectOutputStream s" %}

## Excepciones
[IOException](/Java/IOException/)

## Clase Padre
[StubDelegate](/Java/StubDelegate/)

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
