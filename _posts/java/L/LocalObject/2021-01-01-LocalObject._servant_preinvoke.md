---
title: LocalObject._servant_preinvoke()
permalink: /Java/LocalObject/_servant_preinvoke/
date: 2021-01-11
key: Java.L.LocalObject
category: Java
tags: ['java se', 'org.omg.CORBA', 'java.corba', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.L.LocalObject.metodos valor="_servant_preinvoke" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public ServantObject _servant_preinvoke(String operation, Class expectedType)
~~~

## Parámetros
* **Class expectedType**,  {% include w3api/param_description.html metodo=_dato parametro="Class expectedType" %}
* **String operation**,  {% include w3api/param_description.html metodo=_dato parametro="String operation" %}

## Clase Padre
[LocalObject](/Java/LocalObject/)

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
