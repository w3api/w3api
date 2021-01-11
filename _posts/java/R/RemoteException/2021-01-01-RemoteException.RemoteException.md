---
title: RemoteException.RemoteException()
permalink: Java/RemoteException/RemoteException
date: 2021-01-11
key: JavaJava.R.RemoteException
category: java
tags: ['java se', 'java.rmi', 'java.rmi', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.RemoteException.constructores valor="RemoteException" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public RemoteException()
public RemoteException(String s)
public RemoteException(String s, Throwable cause)
~~~

## Parámetros
* **Throwable cause**,  {% include w3api/param_description.html metodo=_dato parametro="Throwable cause" %}
* **String s**,  {% include w3api/param_description.html metodo=_dato parametro="String s" %}

## Clase Padre
[RemoteException](/Java/RemoteException/)

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
