---
title: UtilDelegate.isLocal()
permalink: Java/UtilDelegate/isLocal
date: 2021-01-11
key: JavaJava.U.UtilDelegate
category: java
tags: ['java se', 'javax.rmi.CORBA', 'java.corba', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.U.UtilDelegate.metodos valor="isLocal" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
boolean isLocal(Stub stub) throws RemoteException
~~~

## Parámetros
* **Stub stub**,  {% include w3api/param_description.html metodo=_dato parametro="Stub stub" %}

## Excepciones
[RemoteException](/Java/RemoteException/)

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
