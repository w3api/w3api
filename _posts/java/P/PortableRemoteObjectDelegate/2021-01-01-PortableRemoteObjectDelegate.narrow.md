---
title: PortableRemoteObjectDelegate.narrow()
permalink: /Java/PortableRemoteObjectDelegate/narrow/
date: 2021-01-11
key: Java.P.PortableRemoteObjectDelegate
category: java
tags: ['java se', 'javax.rmi.CORBA', 'java.corba', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.PortableRemoteObjectDelegate.metodos valor="narrow" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
Object narrow(Object narrowFrom, Class narrowTo) throws ClassCastException
~~~

## Parámetros
* **Class narrowTo**,  {% include w3api/param_description.html metodo=_dato parametro="Class narrowTo" %}
* **Object narrowFrom**,  {% include w3api/param_description.html metodo=_dato parametro="Object narrowFrom" %}

## Excepciones
[ClassCastException](/Java/ClassCastException/)

## Clase Padre
[PortableRemoteObjectDelegate](/Java/PortableRemoteObjectDelegate/)

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
