---
title: Externalizable.writeExternal()
permalink: /Java/Externalizable/writeExternal/
date: 2021-01-11
key: Java.E.Externalizable
category: Java
tags: ['java se', 'java.io', 'java.base', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.E.Externalizable.metodos valor="writeExternal" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void writeExternal(ObjectOutput out) throws IOException
~~~

## Parámetros
* **ObjectOutput out**,  {% include w3api/param_description.html metodo=_dato parametro="ObjectOutput out" %}

## Excepciones
[IOException](/Java/IOException/)

## Clase Padre
[Externalizable](/Java/Externalizable/)

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
