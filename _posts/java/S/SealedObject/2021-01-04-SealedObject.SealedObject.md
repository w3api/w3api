---
title: SealedObject.SealedObject()
permalink: Java/SealedObject/SealedObject
date: 2021-01-04
key: JavaJava.S.SealedObject
category: java
tags: ['java se', 'javax.crypto', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SealedObject.constructores valor="SealedObject" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public SealedObject(Serializable object, Cipher c) throws IOException, IllegalBlockSizeException
protected SealedObject(SealedObject so)
~~~

## Parámetros
* **Serializable object**,  {% include w3api/param_description.html metodo=_data parametro="Serializable object" %}
* **SealedObject so**,  {% include w3api/param_description.html metodo=_data parametro="SealedObject so" %}
* **Cipher c**,  {% include w3api/param_description.html metodo=_data parametro="Cipher c" %}

## Excepciones
[IllegalBlockSizeException](/Java/IllegalBlockSizeException/), [NullPointerException](/Java/NullPointerException/), [IOException](/Java/IOException/)

## Clase Padre
[SealedObject](/Java/SealedObject/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.SealedObject.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
