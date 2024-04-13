---
title: Activatable.inactive()
permalink: /Java/Activatable/inactive/
date: 2021-01-11
key: Java.A.Activatable
category: Java
tags: ['java se', 'java.rmi.activation', 'java.rmi', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.Activatable.metodos valor="inactive" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static boolean inactive(ActivationID id) throws UnknownObjectException, ActivationException, RemoteException
~~~

## Parámetros
* **ActivationID id**,  {% include w3api/param_description.html metodo=_dato parametro="ActivationID id" %}

## Excepciones
[ActivationException](/Java/ActivationException/), [UnknownObjectException](/Java/UnknownObjectException/), [RemoteException](/Java/RemoteException/), [UnsupportedOperationException](/Java/UnsupportedOperationException/)

## Clase Padre
[Activatable](/Java/Activatable/)

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
