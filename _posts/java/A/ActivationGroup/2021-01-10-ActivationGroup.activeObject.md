---
title: ActivationGroup.activeObject()
permalink: Java/ActivationGroup/activeObject
date: 2021-01-10
key: JavaJava.A.ActivationGroup
category: java
tags: ['java se', 'java.rmi.activation', 'java.rmi', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.ActivationGroup.metodos valor="activeObject" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected void activeObject(ActivationID id, MarshalledObject<? extends Remote> mobj) throws ActivationException, UnknownObjectException, RemoteException
public abstract void activeObject(ActivationID id, Remote obj) throws ActivationException, UnknownObjectException, RemoteException
~~~

## Parámetros
* **Remote obj**,  {% include w3api/param_description.html metodo=_dato parametro="Remote obj" %}
* **MarshalledObject&lt;? extends Remote&gt; mobj**,  {% include w3api/param_description.html metodo=_dato parametro="MarshalledObject<? extends Remote> mobj" %}
* **ActivationID id**,  {% include w3api/param_description.html metodo=_dato parametro="ActivationID id" %}

## Excepciones
[UnknownObjectException](/Java/UnknownObjectException/), [RemoteException](/Java/RemoteException/), [ActivationException](/Java/ActivationException/)

## Clase Padre
[ActivationGroup](/Java/ActivationGroup/)

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
