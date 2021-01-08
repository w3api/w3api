---
title: Externalizable.readExternal()
permalink: Java/Externalizable/readExternal
date: 2021-01-04
key: JavaJava.E.Externalizable
category: java
tags: ['java se', 'java.io', 'java.base', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.E.Externalizable.metodos valor="readExternal" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void readExternal(ObjectInput in) throws IOException, ClassNotFoundException
~~~

## Parámetros
* **ObjectInput in**,  {% include w3api/param_description.html metodo=_data parametro="ObjectInput in" %}

## Excepciones
[ClassNotFoundException](/Java/ClassNotFoundException/), [IOException](/Java/IOException/)

## Clase Padre
[Externalizable](/Java/Externalizable/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.E.Externalizable.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
