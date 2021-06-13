---
title: UtilDelegate.registerTarget()
permalink: Java/UtilDelegate/registerTarget
date: 2021-01-11
key: JavaJava.U.UtilDelegate
category: java
tags: ['java se', 'javax.rmi.CORBA', 'java.corba', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.U.UtilDelegate.metodos valor="registerTarget" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void registerTarget(Tie tie, Remote target)
~~~

## Parámetros
* **Remote target**,  {% include w3api/param_description.html metodo=_dato parametro="Remote target" %}
* **Tie tie**,  {% include w3api/param_description.html metodo=_dato parametro="Tie tie" %}

## Excepciones
[NoSuchObjectException](/Java/NoSuchObjectException/)

## Clase Padre
[UtilDelegate](/Java/UtilDelegate/)

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