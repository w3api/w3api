---
title: Activatable.register()
permalink: Java/Activatable/register
date: 2021-01-04
key: JavaJava.A.Activatable
category: java
tags: ['java se', 'java.rmi.activation', 'java.rmi', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.Activatable.metodos valor="register" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static Remote register(ActivationDesc desc) throws UnknownGroupException, ActivationException, RemoteException
~~~

## Parámetros
* **ActivationDesc desc**,  {% include w3api/param_description.html metodo=_data parametro="ActivationDesc desc" %}

## Excepciones
[ActivationException](/Java/ActivationException/), [UnknownGroupException](/Java/UnknownGroupException/), [UnsupportedOperationException](/Java/UnsupportedOperationException/), [RemoteException](/Java/RemoteException/)

## Clase Padre
[Activatable](/Java/Activatable/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.A.Activatable.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
