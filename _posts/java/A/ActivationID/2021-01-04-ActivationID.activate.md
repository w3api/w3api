---
title: ActivationID.activate()
permalink: Java/ActivationID/activate
date: 2021-01-04
key: JavaJava.A.ActivationID
category: java
tags: ['java se', 'java.rmi.activation', 'java.rmi', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.ActivationID.metodos valor="activate" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public Remote activate(boolean force) throws ActivationException, UnknownObjectException, RemoteException
~~~

## Parámetros
* **boolean force**,  {% include w3api/param_description.html metodo=_data parametro="boolean force" %}

## Excepciones
[RemoteException](/Java/RemoteException/), [ActivationException](/Java/ActivationException/), [UnknownObjectException](/Java/UnknownObjectException/)

## Clase Padre
[ActivationID](/Java/ActivationID/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.A.ActivationID.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
