---
title: Activatable.unregister()
permalink: Java/Activatable/unregister
date: 2021-01-10
key: JavaJava.A.Activatable
category: java
tags: ['java se', 'java.rmi.activation', 'java.rmi', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.Activatable.metodos valor="unregister" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static void unregister(ActivationID id) throws UnknownObjectException, ActivationException, RemoteException
~~~

## Parámetros
* **ActivationID id**,  {% include w3api/param_description.html metodo=_dato parametro="ActivationID id" %}

## Excepciones
[UnknownObjectException](/Java/UnknownObjectException/), [RemoteException](/Java/RemoteException/), [UnsupportedOperationException](/Java/UnsupportedOperationException/), [ActivationException](/Java/ActivationException/)

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
