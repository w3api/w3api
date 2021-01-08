---
title: ObjectInputStream.registerValidation()
permalink: Java/ObjectInputStream/registerValidation
date: 2021-01-04
key: JavaJava.O.ObjectInputStream
category: java
tags: ['java se', 'java.io', 'java.base', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.O.ObjectInputStream.metodos valor="registerValidation" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void registerValidation(ObjectInputValidation obj, int prio) throws NotActiveException, InvalidObjectException
~~~

## Parámetros
* **int prio**,  {% include w3api/param_description.html metodo=_data parametro="int prio" %}
* **ObjectInputValidation obj**,  {% include w3api/param_description.html metodo=_data parametro="ObjectInputValidation obj" %}

## Excepciones
[NotActiveException](/Java/NotActiveException/), [InvalidObjectException](/Java/InvalidObjectException/)

## Clase Padre
[ObjectInputStream](/Java/ObjectInputStream/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.O.ObjectInputStream.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
