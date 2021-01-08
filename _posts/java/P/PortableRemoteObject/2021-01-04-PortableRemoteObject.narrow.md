---
title: PortableRemoteObject.narrow()
permalink: Java/PortableRemoteObject/narrow
date: 2021-01-04
key: JavaJava.P.PortableRemoteObject
category: java
tags: ['java se', 'javax.rmi', 'java.corba', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.PortableRemoteObject.metodos valor="narrow" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static Object narrow(Object narrowFrom, Class narrowTo) throws ClassCastException
~~~

## Parámetros
* **Object narrowFrom**,  {% include w3api/param_description.html metodo=_data parametro="Object narrowFrom" %}
* **Class narrowTo**,  {% include w3api/param_description.html metodo=_data parametro="Class narrowTo" %}

## Excepciones
[ClassCastException](/Java/ClassCastException/)

## Clase Padre
[PortableRemoteObject](/Java/PortableRemoteObject/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.P.PortableRemoteObject.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
